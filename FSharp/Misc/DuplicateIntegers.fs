module DuplicateIntegers

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
        (actual - expected)

module Test =

    open System
    open NUnit.Framework
    open Fuchu
    open FsUnit

    [<Tests>]
    let tests =

        testList "SingleDuplicate" [

            for f in [ SingleDuplicate.bruteForce; SingleDuplicate.mathy ] do

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
