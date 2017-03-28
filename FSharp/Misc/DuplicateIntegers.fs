module DuplicateIntegers

open System
open NUnit.Framework
open Fuchu
open FsUnit

module SingleDuplicate =

    // Input  : A list with integers in range 1 .. n and one element is a duplicate.
    // Output : The duplicate integer.

    let rec bruteForce l =
        match l with
        | [] | [_] -> failwith "invalid input"
        | h :: t ->
            match List.tryFind (fun x -> x = h) t with
            | None   -> bruteForce t
            | Some _ -> h

    let mathy l =
        let c = List.length l
        if (c < 2) then failwith "invalid input"
        let n = c - 1
        let expected = (n * (n + 1)) / 2
        let actual = List.sum l
        let dupe = (actual - expected)
        if ((dupe < 1) || (dupe > n)) then failwith "invalid input"
        dupe

    let usingSwap l =

        let swap (a: _[]) x y =
            let tmp = a.[x]
            a.[x] <- a.[y]
            a.[y] <- tmp

        let c = List.length l
        if (c < 2) then failwith "invalid input"
        let n = c - 1
        let a = Array.ofList l
        let mutable result = -1

        for i = 1 to n - 1 do
            let mutable keepLooping = true
            while keepLooping do
                keepLooping <-
                    if (i = a.[i]) then
                        false
                    else
                        if (a.[i] = a.[a.[i]]) then
                            result <- a.[i]
                            false
                        else
                            swap a i a.[i]
                            true

        if (result = -1) then failwith "invalid input"

        result


    [<Tests>]
    let tests =

        testList "SingleDuplicate" [

            for f in [ bruteForce; mathy; usingSwap ] do

                yield testList "Basic" [
                    testCase "4 Element" (fun _ -> f [1;2;3;2] |> should equal 2)
                ]

                yield testList "Negative" [
                    for (n, e) in [ ("Empty List", []); ("Single Element List", [3]); ("Bad List", [3;4]) ] do
                        yield testCase n (fun _ ->
                                          (fun () -> f e |> ignore)
                                          |> should (throwWithMessage "invalid input") typeof<Exception>)
                ]
        ]
