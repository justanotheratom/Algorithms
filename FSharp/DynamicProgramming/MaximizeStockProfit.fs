module MaximizeStockProfit

// Greedy algorithm : Find the optimal solution 'so far'.

open System
open NUnit.Framework
open FsUnit
open Fuchu

let maxProfitRecursive p =

    let rec loop minSoFar maxProfitSoFar rest =
        match rest with
        | [] -> maxProfitSoFar
        | h :: t ->
            let newMin =
                if (h < minSoFar) then h else minSoFar
            let newMaxProfit =
                let profit = h - minSoFar
                if (profit > maxProfitSoFar) then profit else maxProfitSoFar
            loop newMin newMaxProfit t

    match p with
    | [] | [_] -> failwith "Not enough datapoints"
    | h :: t -> loop h Int32.MinValue t

let maxProfitIterative prices =

    if (List.length prices < 2) then
        failwith "Not enough datapoints"

    let mutable minPrice  = Int32.MaxValue
    let mutable maxProfit = Int32.MinValue

    for p in prices do
        // iterative solution requires mutability.
        // And problem with mutability - order of these statements matters!
        maxProfit <- max maxProfit (p - minPrice)
        minPrice  <- min minPrice p

    maxProfit

[<Tests>]
let tests =

    let expect f input output _ =
        f input |> should equal output

    let basicTest f i (input, output) =
        testCase (sprintf "%i" i) <| expect f input output

    let shouldFail f input _ =
        (fun () -> f input |> ignore)
        |> should (throwWithMessage "Not enough datapoints") typeof<Exception>

    let negativeTest f i input =
        testCase (sprintf "%i" i) <| shouldFail f input

    testList "MaximizeStockProfit" [
        for f in [ maxProfitRecursive; maxProfitIterative ] do
            yield testList "Basic" (
                [ ([2;3], 1); ([3;2], -1); ([5;3;8;0], 5); ([5;4;3;2;1], -1); ([1;2;3;4;3;2;1], 3) ]
                |> List.mapi (basicTest f)
            )
            yield testList "Negative" (
                [ []; [2] ]
                |> List.mapi (negativeTest f)
            )
    ]

(*
[<TestFixture>]
type Tests () =

    [<Test>]
    member x.``Basic Tests`` () =
        [ ([2;3], 1); ([0;-1], -1); ([5;3;8;0], 5); ([5;4;3;2;1], -1); ([1;2;3;4;3;2;1], 3) ]
        |> List.iter (fun (i, o) -> maxProfitIterative i |> should equal o)

    [<Test>]
    member x.``Negative Tests`` () =
        [ []; [2] ]
        |> List.iter
            (fun (i) ->
                (fun () -> maxProfitIterative i |> ignore)
                |> should (throwWithMessage "Not enough datapoints") typeof<Exception>)
*)